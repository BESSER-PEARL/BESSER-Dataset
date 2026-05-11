





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_CoatOfArmsLayer  {

    private float scale;
    private String mask;





    private ck2gfx_CoatOfArmsType ck2gfx_coatofarmstype;




    private ck2gfx_Coordinates ck2gfx_coordinates;


    public ck2gfx_CoatOfArmsLayer(
        float scale,        String mask    ) {
        this.scale = scale;
        this.mask = mask;
    }


    public float getScale() {
        return scale;
    }

    public void setScale(float scale) {
        this.scale = scale;
    }
    public String getMask() {
        return mask;
    }

    public void setMask(String mask) {
        this.mask = mask;
    }

    public ck2gfx_CoatOfArmsType getCk2gfx_coatofarmstype() {
        return ck2gfx_coatofarmstype;
    }

    public void setCk2gfx_coatofarmstype(ck2gfx_CoatOfArmsType ck2gfx_coatofarmstype) {
        this.ck2gfx_coatofarmstype = ck2gfx_coatofarmstype;
    }
    public ck2gfx_Coordinates getCk2gfx_coordinates() {
        return ck2gfx_coordinates;
    }

    public void setCk2gfx_coordinates(ck2gfx_Coordinates ck2gfx_coordinates) {
        this.ck2gfx_coordinates = ck2gfx_coordinates;
    }

}