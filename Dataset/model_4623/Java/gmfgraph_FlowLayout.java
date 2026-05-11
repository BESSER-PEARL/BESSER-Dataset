





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FlowLayout extends Layout {

    private String minorAlignment;
    private boolean matchMinorSize;
    private String majorAlignment;
    private boolean vertical;
    private int minorSpacing;
    private int majorSpacing;
    private boolean forceSingleLine;



    public gmfgraph_FlowLayout(
        String minorAlignment,        boolean matchMinorSize,        String majorAlignment,        boolean vertical,        int minorSpacing,        int majorSpacing,        boolean forceSingleLine    ) {
        super(
        );
        this.minorAlignment = minorAlignment;
        this.matchMinorSize = matchMinorSize;
        this.majorAlignment = majorAlignment;
        this.vertical = vertical;
        this.minorSpacing = minorSpacing;
        this.majorSpacing = majorSpacing;
        this.forceSingleLine = forceSingleLine;
    }


    public String getMinoralignment() {
        return minorAlignment;
    }

    public void setMinoralignment(String minorAlignment) {
        this.minorAlignment = minorAlignment;
    }
    public boolean getMatchminorsize() {
        return matchMinorSize;
    }

    public void setMatchminorsize(boolean matchMinorSize) {
        this.matchMinorSize = matchMinorSize;
    }
    public String getMajoralignment() {
        return majorAlignment;
    }

    public void setMajoralignment(String majorAlignment) {
        this.majorAlignment = majorAlignment;
    }
    public boolean getVertical() {
        return vertical;
    }

    public void setVertical(boolean vertical) {
        this.vertical = vertical;
    }
    public int getMinorspacing() {
        return minorSpacing;
    }

    public void setMinorspacing(int minorSpacing) {
        this.minorSpacing = minorSpacing;
    }
    public int getMajorspacing() {
        return majorSpacing;
    }

    public void setMajorspacing(int majorSpacing) {
        this.majorSpacing = majorSpacing;
    }
    public boolean getForcesingleline() {
        return forceSingleLine;
    }

    public void setForcesingleline(boolean forceSingleLine) {
        this.forceSingleLine = forceSingleLine;
    }


}