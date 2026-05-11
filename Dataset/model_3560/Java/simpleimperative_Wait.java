





import java.util.List;
import java.util.ArrayList;

public class simpleimperative_Wait extends Statement {

    private String miliseconds;



    public simpleimperative_Wait(
        String miliseconds    ) {
        super(
        );
        this.miliseconds = miliseconds;
    }


    public String getMiliseconds() {
        return miliseconds;
    }

    public void setMiliseconds(String miliseconds) {
        this.miliseconds = miliseconds;
    }


}