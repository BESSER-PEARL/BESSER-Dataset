





import java.util.List;
import java.util.ArrayList;

public class model_MappingElement extends OnoObject {

    private String value;
    private String key;





    private model_TopicMapSchema model_topicmapschema;


    public model_MappingElement(
        String value,        String key    ) {
        super(
        );
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public model_TopicMapSchema getModel_topicmapschema() {
        return model_topicmapschema;
    }

    public void setModel_topicmapschema(model_TopicMapSchema model_topicmapschema) {
        this.model_topicmapschema = model_topicmapschema;
    }

}