





import java.util.List;
import java.util.ArrayList;

public class gast_annotations_Comment extends annotations_ModelAnnotation, core_SourceEntity {

    private int todoCount;
    private String texts;
    private boolean todo;
    private boolean formal;



    public gast_annotations_Comment(
        int todoCount,        String texts,        boolean todo,        boolean formal    ) {
        super(
        );
        this.todoCount = todoCount;
        this.texts = texts;
        this.todo = todo;
        this.formal = formal;
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
    public boolean getTodo() {
        return todo;
    }

    public void setTodo(boolean todo) {
        this.todo = todo;
    }
    public boolean getFormal() {
        return formal;
    }

    public void setFormal(boolean formal) {
        this.formal = formal;
    }


}