





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FlowLayout extends Layout {

    private boolean matchMinorSize;
    private String minorAlignment;
    private int minorSpacing;
    private boolean vertical;
    private int majorSpacing;
    private String majorAlignment;
    private boolean forceSingleLine;



    public gmfgraph_FlowLayout(
        boolean matchMinorSize,        String minorAlignment,        int minorSpacing,        boolean vertical,        int majorSpacing,        String majorAlignment,        boolean forceSingleLine    ) {
        super(
        );
        this.matchMinorSize = matchMinorSize;
        this.minorAlignment = minorAlignment;
        this.minorSpacing = minorSpacing;
        this.vertical = vertical;
        this.majorSpacing = majorSpacing;
        this.majorAlignment = majorAlignment;
        this.forceSingleLine = forceSingleLine;
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
    public int getMinorspacing() {
        return minorSpacing;
    }

    public void setMinorspacing(int minorSpacing) {
        this.minorSpacing = minorSpacing;
    }
    public boolean getVertical() {
        return vertical;
    }

    public void setVertical(boolean vertical) {
        this.vertical = vertical;
    }
    public int getMajorspacing() {
        return majorSpacing;
    }

    public void setMajorspacing(int majorSpacing) {
        this.majorSpacing = majorSpacing;
    }
    public String getMajoralignment() {
        return majorAlignment;
    }

    public void setMajoralignment(String majorAlignment) {
        this.majorAlignment = majorAlignment;
    }
    public boolean getForcesingleline() {
        return forceSingleLine;
    }

    public void setForcesingleline(boolean forceSingleLine) {
        this.forceSingleLine = forceSingleLine;
    }


}