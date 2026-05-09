





import java.util.List;
import java.util.ArrayList;

public class mMDSL_EmbedCode  {

    private String name;
    private String embeddedcode;





    private mMDSL_EmbedCodeType mmdsl_embedcodetype;




    private mMDSL_EmbedPlatformType mmdsl_embedplatformtype;




    private mMDSL_Root mmdsl_root;


    public mMDSL_EmbedCode(
        String name,        String embeddedcode    ) {
        this.name = name;
        this.embeddedcode = embeddedcode;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmbeddedcode() {
        return embeddedcode;
    }

    public void setEmbeddedcode(String embeddedcode) {
        this.embeddedcode = embeddedcode;
    }

    public mMDSL_EmbedCodeType getMmdsl_embedcodetype() {
        return mmdsl_embedcodetype;
    }

    public void setMmdsl_embedcodetype(mMDSL_EmbedCodeType mmdsl_embedcodetype) {
        this.mmdsl_embedcodetype = mmdsl_embedcodetype;
    }
    public mMDSL_EmbedPlatformType getMmdsl_embedplatformtype() {
        return mmdsl_embedplatformtype;
    }

    public void setMmdsl_embedplatformtype(mMDSL_EmbedPlatformType mmdsl_embedplatformtype) {
        this.mmdsl_embedplatformtype = mmdsl_embedplatformtype;
    }
    public mMDSL_Root getMmdsl_root() {
        return mmdsl_root;
    }

    public void setMmdsl_root(mMDSL_Root mmdsl_root) {
        this.mmdsl_root = mmdsl_root;
    }

}