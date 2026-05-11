





import java.util.List;
import java.util.ArrayList;

public class form_SubmitFormButton extends ConnectableElement, FormButton {






    private List<form_Operation> form_operations;


    public form_SubmitFormButton(
    ) {
        super(
        );
        this.form_operations = new ArrayList<>();
    }

    public form_SubmitFormButton(
        ArrayList<form_Operation> form_operations    ) {
        this.form_operations = form_operations;
    }


    public List<form_Operation> getForm_operations() {
        return form_operations;
    }

    public void addForm_operation(Form_operation form_operation) {
        this.form_operations.add(form_operation);
    }

}