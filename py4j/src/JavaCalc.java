


import py4j.GatewayServer;

public class JavaCalc {

  public float addition(float firstNum, float secondNum) {
    return firstNum + secondNum;
  }
  public float subtraction(float firstNum, float secondNum) {
	    return firstNum - secondNum;
	  }

  public static void main(String[] args) {
    JavaCalc app = new JavaCalc();
    // app is now the gateway.entry_point
    GatewayServer server = new GatewayServer(new JavaCalc(), 25375);
    server.start();
  }
}