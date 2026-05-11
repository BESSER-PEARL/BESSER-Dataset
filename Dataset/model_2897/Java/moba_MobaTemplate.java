





import java.util.List;
import java.util.ArrayList;

public class moba_MobaTemplate extends MobaApplicationFeature {

    private String downloadTemplate;





    private moba_MobaApplication moba_mobaapplication;


    public moba_MobaTemplate(
        String downloadTemplate    ) {
        super(
        );
        this.downloadTemplate = downloadTemplate;
    }


    public String getDownloadtemplate() {
        return downloadTemplate;
    }

    public void setDownloadtemplate(String downloadTemplate) {
        this.downloadTemplate = downloadTemplate;
    }

    public moba_MobaApplication getMoba_mobaapplication() {
        return moba_mobaapplication;
    }

    public void setMoba_mobaapplication(moba_MobaApplication moba_mobaapplication) {
        this.moba_mobaapplication = moba_mobaapplication;
    }

}