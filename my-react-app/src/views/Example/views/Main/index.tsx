import React from 'react';
import { observer, inject } from 'mobx-react';
import { Store } from '@/store';

interface Props {
    name?: string;
    example: Store['example'];
}

interface State {
    content: string;
}

@inject('example')
@observer
export default class Main extends React.Component<Props, State> {
    constructor(props: Props) {
        super(props);
        this.state = {
            content: ''
        };
    }

    componentDidMount() {
        this.setState({ content: 'demo' });
    }

    render() {
        const { content } = this.state;
        return (
            <div>
                <p>
                    this is Main
                    {content}
                </p>
            </div>
        );
    }
}
