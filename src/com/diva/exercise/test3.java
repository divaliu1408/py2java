package com.diva.exercise;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class test3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
		      //需传入的参数
			String fileName1 = "D:\\2018BK\\overfit\\spss.csv";
		      String a = fileName1.substring(0,fileName1.length()-4);
		      System.out.println("start;;;" + a);
		      //设置命令行传入参数
		     String[] argv = new String[] {  "C:\\Users\\lhx\\Anaconda2\\python", "C:\\Users\\lhx\\eclipse-workspace\\py2java\\src\\com\\diva\\exercise\\another(1).py", "D:\\2018BK\\overfit\\spss.csv"};

		      Process pr = Runtime.getRuntime().exec(argv);
		      BufferedReader in = new BufferedReader(new InputStreamReader(pr.getInputStream()));
		      String line;
		      while ((line = in.readLine()) != null) {
		          System.out.println(line);
		      }
		      in.close();
		      pr.waitFor();
		      System.out.println("end");
		  } catch (Exception e) {
		      e.printStackTrace();
		  }
	}

}
