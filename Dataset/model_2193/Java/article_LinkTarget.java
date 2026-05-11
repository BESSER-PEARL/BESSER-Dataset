





import java.util.List;
import java.util.ArrayList;

public class article_LinkTarget extends Identifiable {

    private String tooltip;
    private String defaultLabel;





    private article_Link article_link;


    public article_LinkTarget(
        String tooltip,        String defaultLabel    ) {
        super(
        );
        this.tooltip = tooltip;
        this.defaultLabel = defaultLabel;
    }


    public String getTooltip() {
        return tooltip;
    }

    public void setTooltip(String tooltip) {
        this.tooltip = tooltip;
    }
    public String getDefaultlabel() {
        return defaultLabel;
    }

    public void setDefaultlabel(String defaultLabel) {
        this.defaultLabel = defaultLabel;
    }

    public article_Link getArticle_link() {
        return article_link;
    }

    public void setArticle_link(article_Link article_link) {
        this.article_link = article_link;
    }

}