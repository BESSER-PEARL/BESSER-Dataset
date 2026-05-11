





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_Feature extends FeatureDecl {

    private boolean schema;
    private boolean class_;
    private boolean product;



    public deviceModelingLanguage_Feature(
        boolean schema,        boolean class_,        boolean product    ) {
        super(
        );
        this.schema = schema;
        this.class_ = class_;
        this.product = product;
    }


    public boolean getSchema() {
        return schema;
    }

    public void setSchema(boolean schema) {
        this.schema = schema;
    }
    public boolean getClass_() {
        return class_;
    }

    public void setClass_(boolean class_) {
        this.class_ = class_;
    }
    public boolean getProduct() {
        return product;
    }

    public void setProduct(boolean product) {
        this.product = product;
    }


}