





import java.util.List;
import java.util.ArrayList;

public class gama_EGamaObject  {

    private String colorPicto;
    private String hasError;
    private String name;
    private String error;





    private gama_EVariable gama_evariable;




    private gama_EGamaModel gama_egamamodel;




    private gama_EGamaModel gama_egamamodel;


    public gama_EGamaObject(
        String colorPicto,        String hasError,        String name,        String error    ) {
        this.colorPicto = colorPicto;
        this.hasError = hasError;
        this.name = name;
        this.error = error;
    }


    public String getColorpicto() {
        return colorPicto;
    }

    public void setColorpicto(String colorPicto) {
        this.colorPicto = colorPicto;
    }
    public String getHaserror() {
        return hasError;
    }

    public void setHaserror(String hasError) {
        this.hasError = hasError;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getError() {
        return error;
    }

    public void setError(String error) {
        this.error = error;
    }

    public gama_EVariable getGama_evariable() {
        return gama_evariable;
    }

    public void setGama_evariable(gama_EVariable gama_evariable) {
        this.gama_evariable = gama_evariable;
    }
    public gama_EGamaModel getGama_egamamodel() {
        return gama_egamamodel;
    }

    public void setGama_egamamodel(gama_EGamaModel gama_egamamodel) {
        this.gama_egamamodel = gama_egamamodel;
    }
    public gama_EGamaModel getGama_egamamodel() {
        return gama_egamamodel;
    }

    public void setGama_egamamodel(gama_EGamaModel gama_egamamodel) {
        this.gama_egamamodel = gama_egamamodel;
    }

}