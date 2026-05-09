





import java.util.List;
import java.util.ArrayList;

public class model_types_ImportType extends Type {

    private String referenceURL;
    private String url;
    private String modelInterpreterId;
    private String autoresolve;



    public model_types_ImportType(
        String referenceURL,        String url,        String modelInterpreterId,        String autoresolve    ) {
        super(
        );
        this.referenceURL = referenceURL;
        this.url = url;
        this.modelInterpreterId = modelInterpreterId;
        this.autoresolve = autoresolve;
    }


    public String getReferenceurl() {
        return referenceURL;
    }

    public void setReferenceurl(String referenceURL) {
        this.referenceURL = referenceURL;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getModelinterpreterid() {
        return modelInterpreterId;
    }

    public void setModelinterpreterid(String modelInterpreterId) {
        this.modelInterpreterId = modelInterpreterId;
    }
    public String getAutoresolve() {
        return autoresolve;
    }

    public void setAutoresolve(String autoresolve) {
        this.autoresolve = autoresolve;
    }


}