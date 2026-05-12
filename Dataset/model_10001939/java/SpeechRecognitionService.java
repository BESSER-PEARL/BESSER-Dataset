





import java.util.List;
import java.util.ArrayList;

public class SpeechRecognitionService  {

    private String _attr;
    private boolean grabando;
    private String speechRecognition;





    private ChatService chatservice;




    private Mensaje_Interface mensaje_interface;


    public SpeechRecognitionService(
        String _attr,        boolean grabando,        String speechRecognition    ) {
        this._attr = _attr;
        this.grabando = grabando;
        this.speechRecognition = speechRecognition;
    }


    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }
    public boolean getGrabando() {
        return grabando;
    }

    public void setGrabando(boolean grabando) {
        this.grabando = grabando;
    }
    public String getSpeechrecognition() {
        return speechRecognition;
    }

    public void setSpeechrecognition(String speechRecognition) {
        this.speechRecognition = speechRecognition;
    }

    public ChatService getChatservice() {
        return chatservice;
    }

    public void setChatservice(ChatService chatservice) {
        this.chatservice = chatservice;
    }
    public Mensaje_Interface getMensaje_interface() {
        return mensaje_interface;
    }

    public void setMensaje_interface(Mensaje_Interface mensaje_interface) {
        this.mensaje_interface = mensaje_interface;
    }

}