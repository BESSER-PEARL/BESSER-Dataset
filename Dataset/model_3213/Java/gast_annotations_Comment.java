





import java.util.List;
import java.util.ArrayList;

public class gast_annotations_Comment extends annotations_ModelAnnotation, core_SourceEntity {

    private boolean formal;
    private int todoCount;
    private boolean todo;
    private String texts;



    public gast_annotations_Comment(
        boolean formal,        int todoCount,        boolean todo,        String texts    ) {
        super(
        );
        this.formal = formal;
        this.todoCount = todoCount;
        this.todo = todo;
        this.texts = texts;
    }


    public boolean getFormal() {
        return formal;
    }

    public void setFormal(boolean formal) {
        this.formal = formal;
    }
    public int getTodocount() {
        return todoCount;
    }

    public void setTodocount(int todoCount) {
        this.todoCount = todoCount;
    }
    public boolean getTodo() {
        return todo;
    }

    public void setTodo(boolean todo) {
        this.todo = todo;
    }
    public String getTexts() {
        return texts;
    }

    public void setTexts(String texts) {
        this.texts = texts;
    }


}