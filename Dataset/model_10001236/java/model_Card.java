





import java.util.List;
import java.util.ArrayList;

public class model_Card  {

    private None m_value;
    private None m_color;
    private boolean m_isHidden;



    public model_Card(
        None m_value,        None m_color,        boolean m_isHidden    ) {
        this.m_value = m_value;
        this.m_color = m_color;
        this.m_isHidden = m_isHidden;
    }


    public None getM_value() {
        return m_value;
    }

    public void setM_value(None m_value) {
        this.m_value = m_value;
    }
    public None getM_color() {
        return m_color;
    }

    public void setM_color(None m_color) {
        this.m_color = m_color;
    }
    public boolean getM_ishidden() {
        return m_isHidden;
    }

    public void setM_ishidden(boolean m_isHidden) {
        this.m_isHidden = m_isHidden;
    }


}