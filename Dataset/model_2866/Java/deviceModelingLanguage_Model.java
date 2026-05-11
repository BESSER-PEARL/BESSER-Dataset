





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_Model  {

    private boolean class_;
    private boolean schema;
    private boolean product;



    public deviceModelingLanguage_Model(
        boolean class_,        boolean schema,        boolean product    ) {
        this.class_ = class_;
        this.schema = schema;
        this.product = product;
    }


    public boolean getClass_() {
        return class_;
    }

    public void setClass_(boolean class_) {
        this.class_ = class_;
    }
    public boolean getSchema() {
        return schema;
    }

    public void setSchema(boolean schema) {
        this.schema = schema;
    }
    public boolean getProduct() {
        return product;
    }

    public void setProduct(boolean product) {
        this.product = product;
    }


}