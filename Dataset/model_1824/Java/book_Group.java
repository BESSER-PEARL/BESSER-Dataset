





import java.util.List;
import java.util.ArrayList;

public class book_Group extends Control {






    private List<book_Node> book_nodes;


    public book_Group(
    ) {
        super(
        );
        this.book_nodes = new ArrayList<>();
    }

    public book_Group(
        ArrayList<book_Node> book_nodes    ) {
        this.book_nodes = book_nodes;
    }


    public List<book_Node> getBook_nodes() {
        return book_nodes;
    }

    public void addBook_node(Book_node book_node) {
        this.book_nodes.add(book_node);
    }

}