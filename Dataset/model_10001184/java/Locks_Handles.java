





import java.util.List;
import java.util.ArrayList;

public class Locks_Handles  {

    private String Durable;
    private String Secure;



    public Locks_Handles(
        String Durable,        String Secure    ) {
        this.Durable = Durable;
        this.Secure = Secure;
    }


    public String getDurable() {
        return Durable;
    }

    public void setDurable(String Durable) {
        this.Durable = Durable;
    }
    public String getSecure() {
        return Secure;
    }

    public void setSecure(String Secure) {
        this.Secure = Secure;
    }


}