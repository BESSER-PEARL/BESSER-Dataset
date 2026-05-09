





import java.util.List;
import java.util.ArrayList;

public class library_Library  {

    private String map1;
    private String bookByTitleMap;
    private String options;
    private String name;
    private String uRIs_1;





    private List<library_Book> library_books;




    private List<library_Writer> library_writers;




    private List<library_WriterNameMap> library_writernamemaps;




    private List<library_MapOfDataTypes> library_mapofdatatypess;




    private List<library_Book> library_books;


    public library_Library(
        String map1,        String bookByTitleMap,        String options,        String name,        String uRIs_1    ) {
        this.map1 = map1;
        this.bookByTitleMap = bookByTitleMap;
        this.options = options;
        this.name = name;
        this.uRIs_1 = uRIs_1;
        this.library_books = new ArrayList<>();
        this.library_writers = new ArrayList<>();
        this.library_writernamemaps = new ArrayList<>();
        this.library_mapofdatatypess = new ArrayList<>();
        this.library_books = new ArrayList<>();
    }

    public library_Library(
        String map1,        String bookByTitleMap,        String options,        String name,        String uRIs_1        ArrayList<library_Book> library_books,        ArrayList<library_Writer> library_writers,        ArrayList<library_WriterNameMap> library_writernamemaps,        ArrayList<library_MapOfDataTypes> library_mapofdatatypess,        ArrayList<library_Book> library_books    ) {
        this.map1 = map1;
        this.bookByTitleMap = bookByTitleMap;
        this.options = options;
        this.name = name;
        this.uRIs_1 = uRIs_1;
        this.library_books = library_books;
        this.library_writers = library_writers;
        this.library_writernamemaps = library_writernamemaps;
        this.library_mapofdatatypess = library_mapofdatatypess;
        this.library_books = library_books;
    }

    public String getMap1() {
        return map1;
    }

    public void setMap1(String map1) {
        this.map1 = map1;
    }
    public String getBookbytitlemap() {
        return bookByTitleMap;
    }

    public void setBookbytitlemap(String bookByTitleMap) {
        this.bookByTitleMap = bookByTitleMap;
    }
    public String getOptions() {
        return options;
    }

    public void setOptions(String options) {
        this.options = options;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUris_1() {
        return uRIs_1;
    }

    public void setUris_1(String uRIs_1) {
        this.uRIs_1 = uRIs_1;
    }

    public List<library_Book> getLibrary_books() {
        return library_books;
    }

    public void addLibrary_book(Library_book library_book) {
        this.library_books.add(library_book);
    }
    public List<library_Writer> getLibrary_writers() {
        return library_writers;
    }

    public void addLibrary_writer(Library_writer library_writer) {
        this.library_writers.add(library_writer);
    }
    public List<library_WriterNameMap> getLibrary_writernamemaps() {
        return library_writernamemaps;
    }

    public void addLibrary_writernamemap(Library_writernamemap library_writernamemap) {
        this.library_writernamemaps.add(library_writernamemap);
    }
    public List<library_MapOfDataTypes> getLibrary_mapofdatatypess() {
        return library_mapofdatatypess;
    }

    public void addLibrary_mapofdatatypes(Library_mapofdatatypes library_mapofdatatypes) {
        this.library_mapofdatatypess.add(library_mapofdatatypes);
    }
    public List<library_Book> getLibrary_books() {
        return library_books;
    }

    public void addLibrary_book(Library_book library_book) {
        this.library_books.add(library_book);
    }

}