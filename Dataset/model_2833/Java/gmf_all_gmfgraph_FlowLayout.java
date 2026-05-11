





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_FlowLayout extends Layout {

    private boolean forceSingleLine;
    private int minorSpacing;
    private String majorAlignment;
    private int majorSpacing;
    private boolean vertical;
    private boolean matchMinorSize;
    private String minorAlignment;



    public gmf_all_gmfgraph_FlowLayout(
        boolean forceSingleLine,        int minorSpacing,        String majorAlignment,        int majorSpacing,        boolean vertical,        boolean matchMinorSize,        String minorAlignment    ) {
        super(
        );
        this.forceSingleLine = forceSingleLine;
        this.minorSpacing = minorSpacing;
        this.majorAlignment = majorAlignment;
        this.majorSpacing = majorSpacing;
        this.vertical = vertical;
        this.matchMinorSize = matchMinorSize;
        this.minorAlignment = minorAlignment;
    }


    public boolean getForcesingleline() {
        return forceSingleLine;
    }

    public void setForcesingleline(boolean forceSingleLine) {
        this.forceSingleLine = forceSingleLine;
    }
    public int getMinorspacing() {
        return minorSpacing;
    }

    public void setMinorspacing(int minorSpacing) {
        this.minorSpacing = minorSpacing;
    }
    public String getMajoralignment() {
        return majorAlignment;
    }

    public void setMajoralignment(String majorAlignment) {
        this.majorAlignment = majorAlignment;
    }
    public int getMajorspacing() {
        return majorSpacing;
    }

    public void setMajorspacing(int majorSpacing) {
        this.majorSpacing = majorSpacing;
    }
    public boolean getVertical() {
        return vertical;
    }

    public void setVertical(boolean vertical) {
        this.vertical = vertical;
    }
    public boolean getMatchminorsize() {
        return matchMinorSize;
    }

    public void setMatchminorsize(boolean matchMinorSize) {
        this.matchMinorSize = matchMinorSize;
    }
    public String getMinoralignment() {
        return minorAlignment;
    }

    public void setMinoralignment(String minorAlignment) {
        this.minorAlignment = minorAlignment;
    }


}