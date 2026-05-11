





import java.util.List;
import java.util.ArrayList;

public class nabla_ItemRef  {

    private int inc;
    private int dec;





    private nabla_ArgOrVarRef nabla_argorvarref;




    private nabla_Item nabla_item;




    private nabla_ConnectivityCall nabla_connectivitycall;


    public nabla_ItemRef(
        int inc,        int dec    ) {
        this.inc = inc;
        this.dec = dec;
    }


    public int getInc() {
        return inc;
    }

    public void setInc(int inc) {
        this.inc = inc;
    }
    public int getDec() {
        return dec;
    }

    public void setDec(int dec) {
        this.dec = dec;
    }

    public nabla_ArgOrVarRef getNabla_argorvarref() {
        return nabla_argorvarref;
    }

    public void setNabla_argorvarref(nabla_ArgOrVarRef nabla_argorvarref) {
        this.nabla_argorvarref = nabla_argorvarref;
    }
    public nabla_Item getNabla_item() {
        return nabla_item;
    }

    public void setNabla_item(nabla_Item nabla_item) {
        this.nabla_item = nabla_item;
    }
    public nabla_ConnectivityCall getNabla_connectivitycall() {
        return nabla_connectivitycall;
    }

    public void setNabla_connectivitycall(nabla_ConnectivityCall nabla_connectivitycall) {
        this.nabla_connectivitycall = nabla_connectivitycall;
    }

}