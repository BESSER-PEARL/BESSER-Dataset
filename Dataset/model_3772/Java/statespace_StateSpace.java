





import java.util.List;
import java.util.ArrayList;

public class statespace_StateSpace extends Storage {

    private boolean layoutHideIndizes;
    private int transitionCount;
    private int maxStateDistance;
    private boolean layoutHideLabels;
    private int layoutZoomLevel;
    private int stateCount;
    private int layoutTransitionAttraction;
    private int layoutStateRepulsion;
    private String allParameterKeys;



    public statespace_StateSpace(
        boolean layoutHideIndizes,        int transitionCount,        int maxStateDistance,        boolean layoutHideLabels,        int layoutZoomLevel,        int stateCount,        int layoutTransitionAttraction,        int layoutStateRepulsion,        String allParameterKeys    ) {
        super(
        );
        this.layoutHideIndizes = layoutHideIndizes;
        this.transitionCount = transitionCount;
        this.maxStateDistance = maxStateDistance;
        this.layoutHideLabels = layoutHideLabels;
        this.layoutZoomLevel = layoutZoomLevel;
        this.stateCount = stateCount;
        this.layoutTransitionAttraction = layoutTransitionAttraction;
        this.layoutStateRepulsion = layoutStateRepulsion;
        this.allParameterKeys = allParameterKeys;
    }


    public boolean getLayouthideindizes() {
        return layoutHideIndizes;
    }

    public void setLayouthideindizes(boolean layoutHideIndizes) {
        this.layoutHideIndizes = layoutHideIndizes;
    }
    public int getTransitioncount() {
        return transitionCount;
    }

    public void setTransitioncount(int transitionCount) {
        this.transitionCount = transitionCount;
    }
    public int getMaxstatedistance() {
        return maxStateDistance;
    }

    public void setMaxstatedistance(int maxStateDistance) {
        this.maxStateDistance = maxStateDistance;
    }
    public boolean getLayouthidelabels() {
        return layoutHideLabels;
    }

    public void setLayouthidelabels(boolean layoutHideLabels) {
        this.layoutHideLabels = layoutHideLabels;
    }
    public int getLayoutzoomlevel() {
        return layoutZoomLevel;
    }

    public void setLayoutzoomlevel(int layoutZoomLevel) {
        this.layoutZoomLevel = layoutZoomLevel;
    }
    public int getStatecount() {
        return stateCount;
    }

    public void setStatecount(int stateCount) {
        this.stateCount = stateCount;
    }
    public int getLayouttransitionattraction() {
        return layoutTransitionAttraction;
    }

    public void setLayouttransitionattraction(int layoutTransitionAttraction) {
        this.layoutTransitionAttraction = layoutTransitionAttraction;
    }
    public int getLayoutstaterepulsion() {
        return layoutStateRepulsion;
    }

    public void setLayoutstaterepulsion(int layoutStateRepulsion) {
        this.layoutStateRepulsion = layoutStateRepulsion;
    }
    public String getAllparameterkeys() {
        return allParameterKeys;
    }

    public void setAllparameterkeys(String allParameterKeys) {
        this.allParameterKeys = allParameterKeys;
    }


}