





import java.util.List;
import java.util.ArrayList;

public class adaptiveSystem_Condition extends Node {

    private boolean maximal;
    private boolean marked;
    private boolean minimal;
    private int token;





    private adaptiveSystem_PreNet adaptivesystem_prenet;




    private adaptiveSystem_AdaptiveProcess adaptivesystem_adaptiveprocess;


    public adaptiveSystem_Condition(
        boolean maximal,        boolean marked,        boolean minimal,        int token    ) {
        super(
        );
        this.maximal = maximal;
        this.marked = marked;
        this.minimal = minimal;
        this.token = token;
    }


    public boolean getMaximal() {
        return maximal;
    }

    public void setMaximal(boolean maximal) {
        this.maximal = maximal;
    }
    public boolean getMarked() {
        return marked;
    }

    public void setMarked(boolean marked) {
        this.marked = marked;
    }
    public boolean getMinimal() {
        return minimal;
    }

    public void setMinimal(boolean minimal) {
        this.minimal = minimal;
    }
    public int getToken() {
        return token;
    }

    public void setToken(int token) {
        this.token = token;
    }

    public adaptiveSystem_PreNet getAdaptivesystem_prenet() {
        return adaptivesystem_prenet;
    }

    public void setAdaptivesystem_prenet(adaptiveSystem_PreNet adaptivesystem_prenet) {
        this.adaptivesystem_prenet = adaptivesystem_prenet;
    }
    public adaptiveSystem_AdaptiveProcess getAdaptivesystem_adaptiveprocess() {
        return adaptivesystem_adaptiveprocess;
    }

    public void setAdaptivesystem_adaptiveprocess(adaptiveSystem_AdaptiveProcess adaptivesystem_adaptiveprocess) {
        this.adaptivesystem_adaptiveprocess = adaptivesystem_adaptiveprocess;
    }

}