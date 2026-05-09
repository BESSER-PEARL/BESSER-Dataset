





import java.util.List;
import java.util.ArrayList;

public class model_Person  {

    private String name;





    private model_BookShelf model_bookshelf;




    private List<model_Person> model_persons;




    private List<model_BookShelf> model_bookshelfs;




    private model_DataBase model_database;


    public model_Person(
        String name    ) {
        this.name = name;
        this.model_persons = new ArrayList<>();
        this.model_bookshelfs = new ArrayList<>();
    }

    public model_Person(
        String name        ArrayList<model_Person> model_persons,        ArrayList<model_BookShelf> model_bookshelfs    ) {
        this.name = name;
        this.model_persons = model_persons;
        this.model_bookshelfs = model_bookshelfs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_BookShelf getModel_bookshelf() {
        return model_bookshelf;
    }

    public void setModel_bookshelf(model_BookShelf model_bookshelf) {
        this.model_bookshelf = model_bookshelf;
    }
    public List<model_Person> getModel_persons() {
        return model_persons;
    }

    public void addModel_person(Model_person model_person) {
        this.model_persons.add(model_person);
    }
    public List<model_BookShelf> getModel_bookshelfs() {
        return model_bookshelfs;
    }

    public void addModel_bookshelf(Model_bookshelf model_bookshelf) {
        this.model_bookshelfs.add(model_bookshelf);
    }
    public model_DataBase getModel_database() {
        return model_database;
    }

    public void setModel_database(model_DataBase model_database) {
        this.model_database = model_database;
    }

}