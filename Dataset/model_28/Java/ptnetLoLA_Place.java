





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_Place extends Node {

    private int finalMarking;
    private int token;



    public ptnetLoLA_Place(
        int finalMarking,        int token    ) {
        super(
        );
        this.finalMarking = finalMarking;
        this.token = token;
    }


    public int getFinalmarking() {
        return finalMarking;
    }

    public void setFinalmarking(int finalMarking) {
        this.finalMarking = finalMarking;
    }
    public int getToken() {
        return token;
    }

    public void setToken(int token) {
        this.token = token;
    }


}