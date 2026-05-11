





import java.util.List;
import java.util.ArrayList;

public class afpText_EII extends structuredField {

    private String ImoName;



    public afpText_EII(
        String ImoName    ) {
        super(
        );
        this.ImoName = ImoName;
    }


    public String getImoname() {
        return ImoName;
    }

    public void setImoname(String ImoName) {
        this.ImoName = ImoName;
    }


}