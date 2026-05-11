





import java.util.List;
import java.util.ArrayList;

public class wiki_Revision  {

    private int text_id;
    private String date;
    private String user;





    private wiki_Node wiki_node;




    private wiki_Node wiki_node;




    private wiki_Wiki wiki_wiki;




    private wiki_Node wiki_node;


    public wiki_Revision(
        int text_id,        String date,        String user    ) {
        this.text_id = text_id;
        this.date = date;
        this.user = user;
    }


    public int getText_id() {
        return text_id;
    }

    public void setText_id(int text_id) {
        this.text_id = text_id;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }

    public wiki_Node getWiki_node() {
        return wiki_node;
    }

    public void setWiki_node(wiki_Node wiki_node) {
        this.wiki_node = wiki_node;
    }
    public wiki_Node getWiki_node() {
        return wiki_node;
    }

    public void setWiki_node(wiki_Node wiki_node) {
        this.wiki_node = wiki_node;
    }
    public wiki_Wiki getWiki_wiki() {
        return wiki_wiki;
    }

    public void setWiki_wiki(wiki_Wiki wiki_wiki) {
        this.wiki_wiki = wiki_wiki;
    }
    public wiki_Node getWiki_node() {
        return wiki_node;
    }

    public void setWiki_node(wiki_Node wiki_node) {
        this.wiki_node = wiki_node;
    }

}