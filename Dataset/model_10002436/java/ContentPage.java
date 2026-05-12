





import java.util.List;
import java.util.ArrayList;

public class ContentPage  {

    private None priorityExpiryDate;
    private String externalSource;
    private None address;
    private None author;
    private String references;
    private None media;
    private None date;
    private String priority;
    private boolean active;
    private String state;
    private String tags;
    private String headline;
    private String attribute;
    private String content;
    private String content1;
    private None expiryDate;
    private String title;
    private None publishingDate;





    private AdminUser adminuser;


    public ContentPage(
        None priorityExpiryDate,        String externalSource,        None address,        None author,        String references,        None media,        None date,        String priority,        boolean active,        String state,        String tags,        String headline,        String attribute,        String content,        String content1,        None expiryDate,        String title,        None publishingDate    ) {
        this.priorityExpiryDate = priorityExpiryDate;
        this.externalSource = externalSource;
        this.address = address;
        this.author = author;
        this.references = references;
        this.media = media;
        this.date = date;
        this.priority = priority;
        this.active = active;
        this.state = state;
        this.tags = tags;
        this.headline = headline;
        this.attribute = attribute;
        this.content = content;
        this.content1 = content1;
        this.expiryDate = expiryDate;
        this.title = title;
        this.publishingDate = publishingDate;
    }


    public None getPriorityexpirydate() {
        return priorityExpiryDate;
    }

    public void setPriorityexpirydate(None priorityExpiryDate) {
        this.priorityExpiryDate = priorityExpiryDate;
    }
    public String getExternalsource() {
        return externalSource;
    }

    public void setExternalsource(String externalSource) {
        this.externalSource = externalSource;
    }
    public None getAddress() {
        return address;
    }

    public void setAddress(None address) {
        this.address = address;
    }
    public None getAuthor() {
        return author;
    }

    public void setAuthor(None author) {
        this.author = author;
    }
    public String getReferences() {
        return references;
    }

    public void setReferences(String references) {
        this.references = references;
    }
    public None getMedia() {
        return media;
    }

    public void setMedia(None media) {
        this.media = media;
    }
    public None getDate() {
        return date;
    }

    public void setDate(None date) {
        this.date = date;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getTags() {
        return tags;
    }

    public void setTags(String tags) {
        this.tags = tags;
    }
    public String getHeadline() {
        return headline;
    }

    public void setHeadline(String headline) {
        this.headline = headline;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getContent1() {
        return content1;
    }

    public void setContent1(String content1) {
        this.content1 = content1;
    }
    public None getExpirydate() {
        return expiryDate;
    }

    public void setExpirydate(None expiryDate) {
        this.expiryDate = expiryDate;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public None getPublishingdate() {
        return publishingDate;
    }

    public void setPublishingdate(None publishingDate) {
        this.publishingDate = publishingDate;
    }

    public AdminUser getAdminuser() {
        return adminuser;
    }

    public void setAdminuser(AdminUser adminuser) {
        this.adminuser = adminuser;
    }

}