





import java.util.List;
import java.util.ArrayList;

public class statespace_StateSpace extends Storage {

    private int transitionCount;
    private int layoutStateRepulsion;
    private boolean layoutHideLabels;
    private String allParameterKeys;
    private int maxStateDistance;
    private int layoutTransitionAttraction;
    private int stateCount;
    private boolean layoutHideIndizes;
    private int layoutZoomLevel;



    public statespace_StateSpace(
        int transitionCount,        int layoutStateRepulsion,        boolean layoutHideLabels,        String allParameterKeys,        int maxStateDistance,        int layoutTransitionAttraction,        int stateCount,        boolean layoutHideIndizes,        int layoutZoomLevel    ) {
        super(
        );
        this.transitionCount = transitionCount;
        this.layoutStateRepulsion = layoutStateRepulsion;
        this.layoutHideLabels = layoutHideLabels;
        this.allParameterKeys = allParameterKeys;
        this.maxStateDistance = maxStateDistance;
        this.layoutTransitionAttraction = layoutTransitionAttraction;
        this.stateCount = stateCount;
        this.layoutHideIndizes = layoutHideIndizes;
        this.layoutZoomLevel = layoutZoomLevel;
    }


    public int getTransitioncount() {
        return transitionCount;
    }

    public void setTransitioncount(int transitionCount) {
        this.transitionCount = transitionCount;
    }
    public int getLayoutstaterepulsion() {
        return layoutStateRepulsion;
    }

    public void setLayoutstaterepulsion(int layoutStateRepulsion) {
        this.layoutStateRepulsion = layoutStateRepulsion;
    }
    public boolean getLayouthidelabels() {
        return layoutHideLabels;
    }

    public void setLayouthidelabels(boolean layoutHideLabels) {
        this.layoutHideLabels = layoutHideLabels;
    }
    public String getAllparameterkeys() {
        return allParameterKeys;
    }

    public void setAllparameterkeys(String allParameterKeys) {
        this.allParameterKeys = allParameterKeys;
    }
    public int getMaxstatedistance() {
        return maxStateDistance;
    }

    public void setMaxstatedistance(int maxStateDistance) {
        this.maxStateDistance = maxStateDistance;
    }
    public int getLayouttransitionattraction() {
        return layoutTransitionAttraction;
    }

    public void setLayouttransitionattraction(int layoutTransitionAttraction) {
        this.layoutTransitionAttraction = layoutTransitionAttraction;
    }
    public int getStatecount() {
        return stateCount;
    }

    public void setStatecount(int stateCount) {
        this.stateCount = stateCount;
    }
    public boolean getLayouthideindizes() {
        return layoutHideIndizes;
    }

    public void setLayouthideindizes(boolean layoutHideIndizes) {
        this.layoutHideIndizes = layoutHideIndizes;
    }
    public int getLayoutzoomlevel() {
        return layoutZoomLevel;
    }

    public void setLayoutzoomlevel(int layoutZoomLevel) {
        this.layoutZoomLevel = layoutZoomLevel;
    }


}