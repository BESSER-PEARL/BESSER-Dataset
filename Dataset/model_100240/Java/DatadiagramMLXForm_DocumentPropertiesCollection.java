





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_DocumentPropertiesCollection  {

    private String hyperlinkBase_href;
    private String title;
    private String creator;
    private String subject;
    private String description;
    private String keywords;
    private String buildNumberEdited;
    private String buildNumberCreated;
    private String category;
    private String alternateNames;
    private String template;
    private String company;
    private String manager;



    public DatadiagramMLXForm_DocumentPropertiesCollection(
        String hyperlinkBase_href,        String title,        String creator,        String subject,        String description,        String keywords,        String buildNumberEdited,        String buildNumberCreated,        String category,        String alternateNames,        String template,        String company,        String manager    ) {
        this.hyperlinkBase_href = hyperlinkBase_href;
        this.title = title;
        this.creator = creator;
        this.subject = subject;
        this.description = description;
        this.keywords = keywords;
        this.buildNumberEdited = buildNumberEdited;
        this.buildNumberCreated = buildNumberCreated;
        this.category = category;
        this.alternateNames = alternateNames;
        this.template = template;
        this.company = company;
        this.manager = manager;
    }


    public String getHyperlinkbase_href() {
        return hyperlinkBase_href;
    }

    public void setHyperlinkbase_href(String hyperlinkBase_href) {
        this.hyperlinkBase_href = hyperlinkBase_href;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getCreator() {
        return creator;
    }

    public void setCreator(String creator) {
        this.creator = creator;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }
    public String getBuildnumberedited() {
        return buildNumberEdited;
    }

    public void setBuildnumberedited(String buildNumberEdited) {
        this.buildNumberEdited = buildNumberEdited;
    }
    public String getBuildnumbercreated() {
        return buildNumberCreated;
    }

    public void setBuildnumbercreated(String buildNumberCreated) {
        this.buildNumberCreated = buildNumberCreated;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getAlternatenames() {
        return alternateNames;
    }

    public void setAlternatenames(String alternateNames) {
        this.alternateNames = alternateNames;
    }
    public String getTemplate() {
        return template;
    }

    public void setTemplate(String template) {
        this.template = template;
    }
    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }
    public String getManager() {
        return manager;
    }

    public void setManager(String manager) {
        this.manager = manager;
    }


}