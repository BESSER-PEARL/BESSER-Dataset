





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Points  {

    private String y;
    private String x;





    private mMDSL_Polyline mmdsl_polyline;




    private mMDSL_Polygon mmdsl_polygon;


    public mMDSL_Points(
        String y,        String x    ) {
        this.y = y;
        this.x = x;
    }


    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }

    public mMDSL_Polyline getMmdsl_polyline() {
        return mmdsl_polyline;
    }

    public void setMmdsl_polyline(mMDSL_Polyline mmdsl_polyline) {
        this.mmdsl_polyline = mmdsl_polyline;
    }
    public mMDSL_Polygon getMmdsl_polygon() {
        return mmdsl_polygon;
    }

    public void setMmdsl_polygon(mMDSL_Polygon mmdsl_polygon) {
        this.mmdsl_polygon = mmdsl_polygon;
    }

}