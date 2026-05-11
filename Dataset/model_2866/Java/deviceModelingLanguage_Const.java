





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_Const extends MModifier, Modifier {

    private boolean instance;
    private boolean class_;
    private boolean product;
    private boolean schema;



    public deviceModelingLanguage_Const(
        boolean instance,        boolean class_,        boolean product,        boolean schema    ) {
        super(
        );
        this.instance = instance;
        this.class_ = class_;
        this.product = product;
        this.schema = schema;
    }


    public boolean getInstance() {
        return instance;
    }

    public void setInstance(boolean instance) {
        this.instance = instance;
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
    public boolean getSchema() {
        return schema;
    }

    public void setSchema(boolean schema) {
        this.schema = schema;
    }


}