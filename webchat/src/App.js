import {ChatEngine} from 'react-chat-engine';
import ChatFeed from './components/ChatFeed';

import './App.css';

const App = () => {
    return (
        <ChatEngine
            height="100vh"
            projectID="
            a99999cf-6cb0-4d87-b57f-3a759574f356"
            userName="MK"
            userSecret="CHATENGINE123"
            renderChatFeed={(chatAppProps) => <ChatFeed {... chatAppProps}/>}
            />
    )
}

export default App
