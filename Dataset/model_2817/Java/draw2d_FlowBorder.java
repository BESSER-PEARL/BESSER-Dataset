





import java.util.List;
import java.util.ArrayList;

public class draw2d_FlowBorder extends Border {

    private int leftMargin;
    private int bottomMargin;
    private int rightMargin;
    private int topMargin;



    public draw2d_FlowBorder(
        int leftMargin,        int bottomMargin,        int rightMargin,        int topMargin    ) {
        super(
        );
        this.leftMargin = leftMargin;
        this.bottomMargin = bottomMargin;
        this.rightMargin = rightMargin;
        this.topMargin = topMargin;
    }


    public int getLeftmargin() {
        return leftMargin;
    }

    public void setLeftmargin(int leftMargin) {
        this.leftMargin = leftMargin;
    }
    public int getBottommargin() {
        return bottomMargin;
    }

    public void setBottommargin(int bottomMargin) {
        this.bottomMargin = bottomMargin;
    }
    public int getRightmargin() {
        return rightMargin;
    }

    public void setRightmargin(int rightMargin) {
        this.rightMargin = rightMargin;
    }
    public int getTopmargin() {
        return topMargin;
    }

    public void setTopmargin(int topMargin) {
        this.topMargin = topMargin;
    }


}