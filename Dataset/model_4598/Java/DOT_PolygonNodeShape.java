





import java.util.List;
import java.util.ArrayList;

public class DOT_PolygonNodeShape extends ComplexNodeShape {

    private int distortion;
    private boolean isRegular;
    private int sides;
    private int skew;
    private int orientation;



    public DOT_PolygonNodeShape(
        int distortion,        boolean isRegular,        int sides,        int skew,        int orientation    ) {
        super(
        );
        this.distortion = distortion;
        this.isRegular = isRegular;
        this.sides = sides;
        this.skew = skew;
        this.orientation = orientation;
    }


    public int getDistortion() {
        return distortion;
    }

    public void setDistortion(int distortion) {
        this.distortion = distortion;
    }
    public boolean getIsregular() {
        return isRegular;
    }

    public void setIsregular(boolean isRegular) {
        this.isRegular = isRegular;
    }
    public int getSides() {
        return sides;
    }

    public void setSides(int sides) {
        this.sides = sides;
    }
    public int getSkew() {
        return skew;
    }

    public void setSkew(int skew) {
        this.skew = skew;
    }
    public int getOrientation() {
        return orientation;
    }

    public void setOrientation(int orientation) {
        this.orientation = orientation;
    }


}