





import java.util.List;
import java.util.ArrayList;

public class mMDSL_PathParametersMLT  {

    private String y;
    private String x;





    private mMDSL_SmoothQuadraticBezierCurveTo mmdsl_smoothquadraticbeziercurveto;




    private mMDSL_LineTo mmdsl_lineto;




    private mMDSL_MoveTo mmdsl_moveto;


    public mMDSL_PathParametersMLT(
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

    public mMDSL_SmoothQuadraticBezierCurveTo getMmdsl_smoothquadraticbeziercurveto() {
        return mmdsl_smoothquadraticbeziercurveto;
    }

    public void setMmdsl_smoothquadraticbeziercurveto(mMDSL_SmoothQuadraticBezierCurveTo mmdsl_smoothquadraticbeziercurveto) {
        this.mmdsl_smoothquadraticbeziercurveto = mmdsl_smoothquadraticbeziercurveto;
    }
    public mMDSL_LineTo getMmdsl_lineto() {
        return mmdsl_lineto;
    }

    public void setMmdsl_lineto(mMDSL_LineTo mmdsl_lineto) {
        this.mmdsl_lineto = mmdsl_lineto;
    }
    public mMDSL_MoveTo getMmdsl_moveto() {
        return mmdsl_moveto;
    }

    public void setMmdsl_moveto(mMDSL_MoveTo mmdsl_moveto) {
        this.mmdsl_moveto = mmdsl_moveto;
    }

}