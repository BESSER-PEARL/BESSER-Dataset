





import java.util.List;
import java.util.ArrayList;

public class article_TreeNodeProperty  {

    private String valueImage;
    private String value;
    private String key;





    private List<article_TreeNodeProperty> article_treenodepropertys;


    public article_TreeNodeProperty(
        String valueImage,        String value,        String key    ) {
        this.valueImage = valueImage;
        this.value = value;
        this.key = key;
        this.article_treenodepropertys = new ArrayList<>();
    }

    public article_TreeNodeProperty(
        String valueImage,        String value,        String key        ArrayList<article_TreeNodeProperty> article_treenodepropertys    ) {
        this.valueImage = valueImage;
        this.value = value;
        this.key = key;
        this.article_treenodepropertys = article_treenodepropertys;
    }

    public String getValueimage() {
        return valueImage;
    }

    public void setValueimage(String valueImage) {
        this.valueImage = valueImage;
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

    public List<article_TreeNodeProperty> getArticle_treenodepropertys() {
        return article_treenodepropertys;
    }

    public void addArticle_treenodeproperty(Article_treenodeproperty article_treenodeproperty) {
        this.article_treenodepropertys.add(article_treenodeproperty);
    }

}