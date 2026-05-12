





import java.util.List;
import java.util.ArrayList;

public class Passenger  {

    private boolean check_in;
    private None baggage;
    private String pass;
    private None id;



    public Passenger(
        boolean check_in,        None baggage,        String pass,        None id    ) {
        this.check_in = check_in;
        this.baggage = baggage;
        this.pass = pass;
        this.id = id;
    }


    public boolean getCheck_in() {
        return check_in;
    }

    public void setCheck_in(boolean check_in) {
        this.check_in = check_in;
    }
    public None getBaggage() {
        return baggage;
    }

    public void setBaggage(None baggage) {
        this.baggage = baggage;
    }
    public String getPass() {
        return pass;
    }

    public void setPass(String pass) {
        this.pass = pass;
    }
    public None getId() {
        return id;
    }

    public void setId(None id) {
        this.id = id;
    }


}