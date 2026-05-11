





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwComputing_HwISA extends HwResource {

    private String type;





    private NFP_DataSize nfp_datasize;


    public MARTE_HwComputing_HwISA(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public NFP_DataSize getNfp_datasize() {
        return nfp_datasize;
    }

    public void setNfp_datasize(NFP_DataSize nfp_datasize) {
        this.nfp_datasize = nfp_datasize;
    }

}