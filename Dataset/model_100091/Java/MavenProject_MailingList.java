





import java.util.List;
import java.util.ArrayList;

public class MavenProject_MailingList  {

    private String otherArchives;
    private String unsubscribe;
    private String archive;
    private String subscribe;
    private String post;
    private String name;



    public MavenProject_MailingList(
        String otherArchives,        String unsubscribe,        String archive,        String subscribe,        String post,        String name    ) {
        this.otherArchives = otherArchives;
        this.unsubscribe = unsubscribe;
        this.archive = archive;
        this.subscribe = subscribe;
        this.post = post;
        this.name = name;
    }


    public String getOtherarchives() {
        return otherArchives;
    }

    public void setOtherarchives(String otherArchives) {
        this.otherArchives = otherArchives;
    }
    public String getUnsubscribe() {
        return unsubscribe;
    }

    public void setUnsubscribe(String unsubscribe) {
        this.unsubscribe = unsubscribe;
    }
    public String getArchive() {
        return archive;
    }

    public void setArchive(String archive) {
        this.archive = archive;
    }
    public String getSubscribe() {
        return subscribe;
    }

    public void setSubscribe(String subscribe) {
        this.subscribe = subscribe;
    }
    public String getPost() {
        return post;
    }

    public void setPost(String post) {
        this.post = post;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}