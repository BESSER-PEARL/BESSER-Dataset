





import java.util.List;
import java.util.ArrayList;

public class mMDSL_PathParametersHV  {

    private String x;





    private mMDSL_HorizontalLineTo mmdsl_horizontallineto;




    private mMDSL_VerticalLineTo mmdsl_verticallineto;


    public mMDSL_PathParametersHV(
        String x    ) {
        this.x = x;
    }


    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }

    public mMDSL_HorizontalLineTo getMmdsl_horizontallineto() {
        return mmdsl_horizontallineto;
    }

    public void setMmdsl_horizontallineto(mMDSL_HorizontalLineTo mmdsl_horizontallineto) {
        this.mmdsl_horizontallineto = mmdsl_horizontallineto;
    }
    public mMDSL_VerticalLineTo getMmdsl_verticallineto() {
        return mmdsl_verticallineto;
    }

    public void setMmdsl_verticallineto(mMDSL_VerticalLineTo mmdsl_verticallineto) {
        this.mmdsl_verticallineto = mmdsl_verticallineto;
    }

}