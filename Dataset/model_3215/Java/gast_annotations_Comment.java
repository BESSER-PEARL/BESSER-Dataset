





import java.util.List;
import java.util.ArrayList;

public class gast_annotations_Comment extends annotations_ModelAnnotation, core_SourceEntity {

    private boolean todo;
    private int todoCount;
    private String texts;
    private boolean formal;



    public gast_annotations_Comment(
        boolean todo,        int todoCount,        String texts,        boolean formal    ) {
        super(
        );
        this.todo = todo;
        this.todoCount = todoCount;
        this.texts = texts;
        this.formal = formal;
    }


    public boolean getTodo() {
        return todo;
    }

    public void setTodo(boolean todo) {
        this.todo = todo;
    }
    public int getTodocount() {
        return todoCount;
    }

    public void setTodocount(int todoCount) {
        this.todoCount = todoCount;
    }
    public String getTexts() {
        return texts;
    }

    public void setTexts(String texts) {
        this.texts = texts;
    }
    public boolean getFormal() {
        return formal;
    }

    public void setFormal(boolean formal) {
        this.formal = formal;
    }


}