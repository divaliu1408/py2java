package com.diva.exercise;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Properties;

import org.python.apache.xml.serialize.LineSeparator;
import org.python.icu.text.StringPrep;
import org.python.util.PythonInterpreter;


public class usePython {

	public static void main(String[] args)  {
		try {
            //需传入的参数
            String a ="divaliu";
            System.out.println("start;;;" + a);
            //设置命令行传入参数
            String predictPath = "D:\\2018BK\\overfit\\overfitPredict.py";
            String learnPath = "D:\\2018BK\\overfit\\overfitLearn.py";
            String testPath = "C:\\Users\\lhx\\eclipse-workspace\\py2java\\src\\com\\diva\\exercise\\api._test.py";
            String anotherPath = "C:\\Users\\lhx\\eclipse-workspace\\py2java\\src\\com\\diva\\exercise\\another(1).py";
            String[] xStrings = new String[40];
            for (int i = 0;i<xStrings.length;i++) {
            	xStrings[i] = ""+(i+1);
            }
            String[] args1 = new String[] { "C:\\Users\\lhx\\Anaconda2\\python",predictPath,"NAMA.txt"};
            String[] args2 = new String[args1.length + xStrings.length];
            System.arraycopy(args1, 0, args2, 0, args1.length);
            System.arraycopy(xStrings, 0, args2, args1.length, xStrings.length);
//            for (String strx : args2) {
//            	System.out.println(strx);
//            }
            Process pr = Runtime.getRuntime().exec(args2);

            BufferedReader in = new BufferedReader(new InputStreamReader(pr.getInputStream()));
            String line;
            String[] lines = new String[20];
            int i = 0;
            while ((line = in.readLine()) != null) {
            	lines[i] = line;
                System.out.println(line);
                i++;
            }
//            String coefficient = lines[0];
//            String s = lines[1];
//            String path = lines[2];
//            System.out.println("coefficient:\n" +coefficient+"\ns:"+s+"\npath:"+path);
            in.close();
            pr.waitFor();
            System.out.println("end");
        } catch (Exception e) {
            e.printStackTrace();
        }

	}



}
