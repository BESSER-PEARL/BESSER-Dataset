





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_Place extends Node {

    private int token;
    private int finalMarking;



    public ptnetLoLA_Place(
        int token,        int finalMarking    ) {
        super(
        );
        this.token = token;
        this.finalMarking = finalMarking;
    }


    public int getToken() {
        return token;
    }

    public void setToken(int token) {
        this.token = token;
    }
    public int getFinalmarking() {
        return finalMarking;
    }

    public void setFinalmarking(int finalMarking) {
        this.finalMarking = finalMarking;
    }


}