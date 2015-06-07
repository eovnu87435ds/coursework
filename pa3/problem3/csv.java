/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.*;
import java.util.*;
/**
 *
 * @author eovnu_000
 */
public class csv {
    private BufferedReader input;
	private ArrayList field;

	public csv()
	{
		
	}
	
        private static ArrayList split(String csvline, String sep)
	{
		ArrayList list = new ArrayList();
		int i, j;

		if (csvline.length() == 0)
			return(list);

		i = 0;
		do {
			if (i < csvline.length() && csvline.charAt(i) == '"') {
				StringBuffer field = new StringBuffer();
				j = advquoted(csvline, ++i, field);
				list.add(field.toString());
			} else {
				j = csvline.indexOf(sep, i);
				if (j == -1)
					j = csvline.length();
				list.add(csvline.substring(i, j));
			}
			i = j + sep.length();
		} while (j < csvline.length());

		return(list);
	}
        
        private static int advquoted(String s, int i, StringBuffer field)
	{
		field.setLength(0);
		for ( ; i < s.length(); i++) {
			if (s.charAt(i) == '"' && ++i < s.length() && s.charAt(++i) != '"') {
				int j = s.indexOf(",", i);
				if (j == -1)
					j = s.length();
				field.append(s.substring(i, j));
				i = j;
				break;
			}
			field.append(s.charAt(i));
		}

		return(i);
	}
        
	public String getline() throws IOException
	{
            this.input = new BufferedReader(new InputStreamReader(System.in));
		String line;
		line = input.readLine();
		if (line == null){
			return(null);
                }
		field = split(line, ",");
		return(line);
	}

	public String getfield(int n)
	{
		return((String) field.get(n));
	}

	public int getnfield()
	{
		return(field.size());
	}

	public static void main(String[] args) throws IOException
	{
		csv mycsv;
		mycsv = new csv();
                String line = " ";
		while (line != null) {
                    line = mycsv.getline();
			System.out.println("line = `" + line + "'");
			for (int i = 0; i < mycsv.getnfield(); i++) {
				System.out.println("field[" + i + "] = `"
					+ mycsv.getfield(i) + "'");

			}//end for
			line = null;
		}//end while
	}//end main
}//end class
