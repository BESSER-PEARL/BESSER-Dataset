





import java.util.List;
import java.util.ArrayList;

public class ktest401_World  {






    private List<ktest401_Article> ktest401_articles;




    private List<ktest401_Thing> ktest401_things;


    public ktest401_World(
    ) {
        this.ktest401_articles = new ArrayList<>();
        this.ktest401_things = new ArrayList<>();
    }

    public ktest401_World(
        ArrayList<ktest401_Article> ktest401_articles,        ArrayList<ktest401_Thing> ktest401_things    ) {
        this.ktest401_articles = ktest401_articles;
        this.ktest401_things = ktest401_things;
    }


    public List<ktest401_Article> getKtest401_articles() {
        return ktest401_articles;
    }

    public void addKtest401_article(Ktest401_article ktest401_article) {
        this.ktest401_articles.add(ktest401_article);
    }
    public List<ktest401_Thing> getKtest401_things() {
        return ktest401_things;
    }

    public void addKtest401_thing(Ktest401_thing ktest401_thing) {
        this.ktest401_things.add(ktest401_thing);
    }

}