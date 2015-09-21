import tutorial.*;
import shared.*;

import org.apache.thrift.TException;
import org.apache.thrift.transport.TSSLTransportFactory;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TSSLTransportFactory.TSSLTransportParameters;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;

public class JavaClient {
	  public static void main(String [] args) {

		  try {
		      TTransport transport;
		     
		        transport = new TSocket("localhost", 9090);
		        transport.open();
		      
		        TProtocol protocol = new  TBinaryProtocol(transport);
		      Calculator.Client client = new Calculator.Client(protocol);

		      perform(client);

		      transport.close();
		    } catch (TException x) {
		      x.printStackTrace();
		    } 
		  }

		  private static void perform(Calculator.Client client) throws TException
		  {
		    client.ping();
		    System.out.println("ping()");

		    int sum = client.add(1,1);
		    System.out.println("1+1=" + sum);

		    Work work = new Work();


		  }
		}