





import java.util.List;
import java.util.ArrayList;

public class customers_USAddress extends Address {

    private String state;



    public customers_USAddress(
        String state    ) {
        super(
        );
        this.state = state;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }


}