





import java.util.List;
import java.util.ArrayList;

public class model_types_ImportType extends Type {

    private String referenceURL;
    private String autoresolve;
    private String modelInterpreterId;
    private String url;



    public model_types_ImportType(
        String referenceURL,        String autoresolve,        String modelInterpreterId,        String url    ) {
        super(
        );
        this.referenceURL = referenceURL;
        this.autoresolve = autoresolve;
        this.modelInterpreterId = modelInterpreterId;
        this.url = url;
    }


    public String getReferenceurl() {
        return referenceURL;
    }

    public void setReferenceurl(String referenceURL) {
        this.referenceURL = referenceURL;
    }
    public String getAutoresolve() {
        return autoresolve;
    }

    public void setAutoresolve(String autoresolve) {
        this.autoresolve = autoresolve;
    }
    public String getModelinterpreterid() {
        return modelInterpreterId;
    }

    public void setModelinterpreterid(String modelInterpreterId) {
        this.modelInterpreterId = modelInterpreterId;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}