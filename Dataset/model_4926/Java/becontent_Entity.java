





import java.util.List;
import java.util.ArrayList;

public class becontent_Entity extends DefinitionItem {

    private String rssFilter;
    private String name;
    private String variableName;
    private String presentationString;
    private boolean isOwned;





    private becontent_Channel becontent_channel;




    private becontent_SelectFromReference becontent_selectfromreference;




    private becontent_CustomRelation becontent_customrelation;




    private becontent_Channel becontent_channel;




    private becontent_CustomRelation becontent_customrelation;




    private becontent_RadioFromReference becontent_radiofromreference;




    private becontent_Handler becontent_handler;


    public becontent_Entity(
        String rssFilter,        String name,        String variableName,        String presentationString,        boolean isOwned    ) {
        super(
        );
        this.rssFilter = rssFilter;
        this.name = name;
        this.variableName = variableName;
        this.presentationString = presentationString;
        this.isOwned = isOwned;
    }


    public String getRssfilter() {
        return rssFilter;
    }

    public void setRssfilter(String rssFilter) {
        this.rssFilter = rssFilter;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }
    public String getPresentationstring() {
        return presentationString;
    }

    public void setPresentationstring(String presentationString) {
        this.presentationString = presentationString;
    }
    public boolean getIsowned() {
        return isOwned;
    }

    public void setIsowned(boolean isOwned) {
        this.isOwned = isOwned;
    }

    public becontent_Channel getBecontent_channel() {
        return becontent_channel;
    }

    public void setBecontent_channel(becontent_Channel becontent_channel) {
        this.becontent_channel = becontent_channel;
    }
    public becontent_SelectFromReference getBecontent_selectfromreference() {
        return becontent_selectfromreference;
    }

    public void setBecontent_selectfromreference(becontent_SelectFromReference becontent_selectfromreference) {
        this.becontent_selectfromreference = becontent_selectfromreference;
    }
    public becontent_CustomRelation getBecontent_customrelation() {
        return becontent_customrelation;
    }

    public void setBecontent_customrelation(becontent_CustomRelation becontent_customrelation) {
        this.becontent_customrelation = becontent_customrelation;
    }
    public becontent_Channel getBecontent_channel() {
        return becontent_channel;
    }

    public void setBecontent_channel(becontent_Channel becontent_channel) {
        this.becontent_channel = becontent_channel;
    }
    public becontent_CustomRelation getBecontent_customrelation() {
        return becontent_customrelation;
    }

    public void setBecontent_customrelation(becontent_CustomRelation becontent_customrelation) {
        this.becontent_customrelation = becontent_customrelation;
    }
    public becontent_RadioFromReference getBecontent_radiofromreference() {
        return becontent_radiofromreference;
    }

    public void setBecontent_radiofromreference(becontent_RadioFromReference becontent_radiofromreference) {
        this.becontent_radiofromreference = becontent_radiofromreference;
    }
    public becontent_Handler getBecontent_handler() {
        return becontent_handler;
    }

    public void setBecontent_handler(becontent_Handler becontent_handler) {
        this.becontent_handler = becontent_handler;
    }

}