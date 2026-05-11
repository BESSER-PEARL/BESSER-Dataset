





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_Const extends Modifier, MModifier {

    private boolean schema;
    private boolean class_;
    private boolean instance;
    private boolean product;



    public deviceModelingLanguage_Const(
        boolean schema,        boolean class_,        boolean instance,        boolean product    ) {
        super(
        );
        this.schema = schema;
        this.class_ = class_;
        this.instance = instance;
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
    public boolean getInstance() {
        return instance;
    }

    public void setInstance(boolean instance) {
        this.instance = instance;
    }
    public boolean getProduct() {
        return product;
    }

    public void setProduct(boolean product) {
        this.product = product;
    }


}