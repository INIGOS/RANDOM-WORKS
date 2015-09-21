import extract.*;

import org.apache.thrift.TException;
import org.apache.thrift.transport.TSSLTransportFactory;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TSSLTransportFactory.TSSLTransportParameters;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;

public class ExtractClient {
	  public static void main(String [] args) {
		  int text;
		  int output;

		  try {
		      TTransport transport;
		     
		        transport = new TSocket("localhost", 9070);
		        transport.open();
		      
		        TProtocol protocol = new  TBinaryProtocol(transport);
		      extratcionservice.Client client = new extratcionservice.Client(protocol);

		      perform(client);

		      transport.close();
		    } catch (TException x) {
		      x.printStackTrace();
		    } 
		  }

		  private static void perform(extratcionservice.Client client) throws TException
		  {
		    client.ping();
		    System.out.println("ping()");

 String text = "hey hello :p , today is tuesday :) rofl and LOL the weather is :p too hot @ chennai :( :p lol , ok ciao ";
	String output = client.extract(text);
System.out.println(output);

		    


		  }
		}